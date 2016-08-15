module.exports =
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	var _react = __webpack_require__(1);

	var _react2 = _interopRequireDefault(_react);

	__webpack_require__(2);

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

	__webpack_require__(6).polyfill();
	__webpack_require__(7);

	var App = _react2.default.createClass({
	  displayName: 'App',

	  getInitialState: function getInitialState() {
	    return { message: '' };
	  },
	  componentWillMount: function componentWillMount() {
	    this.loadData();
	  },
	  loadData: function loadData() {
	    var _this = this;

	    fetch('http://localhost:8000/test').then(function (response) {
	      if (response.status >= 400) {
	        throw new Error("Bad response from server");
	      }
	      return response.json();
	    }).then(function (data) {
	      _this.setState({ message: data.message });
	    });
	  },
	  render: function render() {
	    return _react2.default.createElement(
	      'div',
	      { className: 'message' },
	      'Message: ',
	      this.state.message
	    );
	  }
	});

	module.exports = App;

/***/ },
/* 1 */
/***/ function(module, exports) {

	module.exports = require("react");

/***/ },
/* 2 */
/***/ function(module, exports) {

	// removed by extract-text-webpack-plugin

/***/ },
/* 3 */,
/* 4 */,
/* 5 */,
/* 6 */
/***/ function(module, exports) {

	module.exports = require("es6-promise");

/***/ },
/* 7 */
/***/ function(module, exports) {

	module.exports = require("isomorphic-fetch");

/***/ }
/******/ ]);