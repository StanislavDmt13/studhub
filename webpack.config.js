const fs = require("fs");
const path = require("path");
const { IgnorePlugin } = require("webpack");
const { parse } = require("sass-variable-parser");
const WebpackNotifierPlugin = require("webpack-notifier");
const tsImportPluginFactory = require("ts-import-plugin");
const { BundleAnalyzerPlugin } = require("webpack-bundle-analyzer");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CleanTerminalPlugin = require("clean-terminal-webpack-plugin");

const isDev = process.env.NODE_ENV === "development";
const isProd = process.env.NODE_ENV === "production";
const isStats = process.env.NODE_ENV === "statistic";

const getPath = (dir) => path.resolve(__dirname, dir);

const paths = {
  index: getPath("frontend/src/index.tsx"),
  src: getPath("frontend/src"),
  appHtml: getPath("templates"),
  build: getPath("frontend/static/dist/"),
  appNodeModules: getPath("node_modules"),
  appTsConfig: getPath("tsconfig.json"),
  variablesLess: getPath("frontend/src/assets/styles/variables.less"),
};

module.exports = {
  entry: path.resolve(paths.src, "index.tsx"),
  devtool: isDev && "source-map", // Enable sourcemaps for debugging webpack"s output.

  output: {
    publicPath: "/static/dist/",
    path: path.join(__dirname, "./frontend/static/dist/"),
    filename: isDev ? "main.min.js" : "[name].[contenthash:8].min.js",
    chunkFilename: isDev
      ? "[name].chunk.min.js"
      : "[name].[contenthash:8].chunk.min.js",
  },

  stats: isDev ? "errors-warnings" : "normal",

  performance: {
    hints: false,
    maxAssetSize: Infinity,
    maxEntrypointSize: Infinity,
  },

  optimization: {
    splitChunks: {
      chunks: "all",
    },
  },

  resolve: {
    extensions: [".ts", ".tsx", ".js", "scss"], // Resolvable extensions.
    modules: [
      // path to app, for absolute import
      paths.src,
      path.resolve(__dirname, "node_modules"),
    ],
  },

  module: {
    rules: [
      {
        test: /\.ts(x?)$/,
        exclude: /node_modeles/,
        use: [
          {
            loader: "ts-loader",
            options: {
              getCustomTransformers: () => ({
                before: [
                  tsImportPluginFactory([
                    {
                      style: true,
                      libraryName: "antd",
                      libraryDirectory: "lib",
                    },
                    {
                      style: (name) => `${name}/index.less`,
                      camel2DashComponentName: false,
                      libraryName: "@datawizio/react-components",
                      libraryDirectory: "es/components",
                    },
                    {
                      style: false,
                      camel2DashComponentName: false,
                      libraryName: "@ant-design/icons",
                      libraryDirectory: (moduleName) => moduleName,
                    },
                  ]),
                ],
              }),
            },
          },
        ],
      },

      {
        test: /\.less$/,
        use: [
          "style-loader",
          "css-loader",
          {
            loader: "less-loader",
            options: {
              lessOptions: {
                javascriptEnabled: true,
              },
            },
          },
        ],
      },

      {
        test: /\.scss$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },

      {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },

      {
        enforce: "pre",
        test: /\.js$/,
        loader: "source-map-loader", // All output ".js" files will have any sourcemaps re-processed by "source-map-loader".
      },
    ],
  },

  plugins: [
    new CleanWebpackPlugin(),

    isDev && new CleanTerminalPlugin(),

    new IgnorePlugin({
      contextRegExp: /moment$/,
      resourceRegExp: /^\.\/locale$/,
    }),

    new HtmlWebpackPlugin({
      template: path.resolve(paths.appHtml, "base.dist.html"),
      filename: path.resolve(paths.appHtml, "base.html"),
      inject: false,
    }),

    isDev && new WebpackNotifierPlugin({ alwaysNotify: true }),

    isStats && new BundleAnalyzerPlugin(),
  ].filter(Boolean),
};
