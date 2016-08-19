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

	var _menuForm = __webpack_require__(6);

	var _menuForm2 = _interopRequireDefault(_menuForm);

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

	__webpack_require__(7).polyfill();
	__webpack_require__(8);

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
	      _react2.default.createElement(_menuForm2.default, null),
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
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	Object.defineProperty(exports, "__esModule", {
	  value: true
	});

	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

	var _react = __webpack_require__(1);

	var _react2 = _interopRequireDefault(_react);

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

	__webpack_require__(7).polyfill();
	__webpack_require__(8);

	var MenuForm = function (_React$Component) {
	  _inherits(MenuForm, _React$Component);

	  function MenuForm(props) {
	    _classCallCheck(this, MenuForm);

	    var _this = _possibleConstructorReturn(this, Object.getPrototypeOf(MenuForm).call(this, props));

	    _this.handleRadio = _this.handleRadio.bind(_this);
	    _this.handleTitle = _this.handleTitle.bind(_this);
	    _this.handleSubmit = _this.handleSubmit.bind(_this);
	    _this.state = {
	      chef: 1,
	      title: '',
	      delivery: true
	    };
	    return _this;
	  }

	  _createClass(MenuForm, [{
	    key: 'handleTitle',
	    value: function handleTitle(e) {
	      this.setState({ title: e.target.value });
	    }
	  }, {
	    key: 'handleRadio',
	    value: function handleRadio(e) {
	      this.setState({ delivery: e.target.value });
	    }
	  }, {
	    key: 'handleSubmit',
	    value: function handleSubmit(e) {
	      e.preventDefault();
	      console.log(this.state);
	      fetch('http://localhost:8000/menus/', {
	        method: 'POST',
	        headers: new Headers({
	          'Content-Type': 'application/json',
	          Accept: 'application/json'
	        }),
	        body: {
	          "title": this.state.title,
	          "chef": this.state.chef,
	          "delivery": this.state.delivery
	        }
	      }).then(function (res) {
	        console.log(res);
	      }).then(function (json) {
	        console.log(json);
	      });
	    }

	    // componentWillMount: function() {

	  }, {
	    key: 'render',
	    value: function render() {
	      return _react2.default.createElement(
	        'div',
	        null,
	        _react2.default.createElement(
	          'form',
	          { onSubmit: this.handleSubmit },
	          _react2.default.createElement('input', { type: 'text', onChange: this.handleTitle }),
	          _react2.default.createElement('br', null),
	          _react2.default.createElement(
	            'fieldset',
	            null,
	            _react2.default.createElement(
	              'label',
	              { htmlFor: 'DeliveryMethod' },
	              'Pickup'
	            ),
	            _react2.default.createElement('input', { type: 'radio', name: 'DeliveryMethod', value: 'True', onChange: this.handleRadio }),
	            _react2.default.createElement('br', null),
	            _react2.default.createElement(
	              'label',
	              { htmlFor: 'DeliveryMethod' },
	              'Delivery'
	            ),
	            _react2.default.createElement('input', { type: 'radio', name: 'DeliveryMethod', value: 'False', onChange: this.handleRadio })
	          ),
	          _react2.default.createElement('input', { type: 'submit', value: 'Submit' })
	        )
	      );
	    }
	  }]);

	  return MenuForm;
	}(_react2.default.Component);

	exports.default = MenuForm;

/***/ },
/* 7 */
/***/ function(module, exports) {

	module.exports = require("es6-promise");

/***/ },
/* 8 */
/***/ function(module, exports) {

	module.exports = require("isomorphic-fetch");

/***/ }
/******/ ]);