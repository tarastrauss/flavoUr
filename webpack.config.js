//require dependencies
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')
var ExtractTextPlugin = require('extract-text-webpack-plugin')

module.exports = {
  //base directory for resolving entry option
  context: __dirname,
  //the entry point created from earlier.
  entry: './shared/templates/index.js',

  output: {
    //destination of compiled bundle
    path: path.resolve('./public/bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    //stores data about bundles.
    new BundleTracker({
      filename: './webpack-stats.json'
    }),
    new ExtractTextPlugin('style.css', { allChunks: true}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'window.jQuery': 'jquery'
    })
  ],

  module: {
    loaders: [
      { test: /\.css$/, loader: "style-loader!css-loader" },
      //regexp that tells webpack to use following loaders on .js & .jsx files
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        //uses babel loader
        loader: 'babel-loader',
        query: {
          //specifies that webpack is handling react.js
          presets: ['react']
        }
      }
    ]
  },

  resolve: {
    //tells webpack where to look for modules
    modulesDirectories: ['node_modules'],
    extensions: ['', '.js', '.jsx']
  }
}
