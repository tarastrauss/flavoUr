// //require dependencies
const path = require('path');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const webpack = require('webpack');
const CLIENT_DIR = path.resolve(__dirname, 'shared');
const SERVER_DIR = path.resolve(__dirname, 'server/generated');
const DIST_DIR = path.resolve(__dirname, 'dist');

const loaders = [{
    test: /\.js$/,
    include: CLIENT_DIR,
    loader: 'babel-loader',
    query: {
      presets: ['es2015', 'react']
    }
  },
  {
    test: /\.less$/,
    loader: ExtractTextPlugin.extract('style-loader', 'css-loader!less-loader')

  }
];

module.exports = [
  {
    name: 'client',
    target: 'web',
    context: CLIENT_DIR,
    entry: './index.js',
    output: {
      path: DIST_DIR,
      filename: 'bundle.js'
    },
    module: {
      loaders: loaders
    },
    resolve: {
      alias: {
        components: path.resolve(CLIENT_DIR, 'components')
      }
    },
    plugins: [
      new ExtractTextPlugin('bundle.css', {allChunks: true})
    ]
  },
  {
    name: 'server',
    target: 'node',
    context: CLIENT_DIR,
    entry: {
      app: 'components/app/index.js'
    },
    output: {
      path: SERVER_DIR,
      filename: '[name].js',
      libraryTarget: 'commonjs2'
    },
    externals: /^[a-z\-0-9]+$/,
    module: {
      loaders: loaders
    },
    resolve: {
      alias: {
        components: path.resolve(CLIENT_DIR, 'components')
      }
    },
    plugins: [
      new ExtractTextPlugin('[name].css'),
      new webpack.ProvidePlugin({
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery'
      })
    ]
  }
];
