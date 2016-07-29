//require dependencies
var path = require('path')
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
  //base directory for resolving entry option
  context: __dirname,
  //the entry point created from earlier.
  entry: './flavoUr/templates/flavoUr/index.js',

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

    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      'windor.jQuery': 'jquery'
    })
  ],

  module: {
    loaders: [

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
