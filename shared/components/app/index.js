import React from 'react';
import {} from './style.less';
require('es6-promise').polyfill();
require('isomorphic-fetch');

var App = React.createClass({
  getInitialState: function() {
    return {message: ''};
  },
  componentWillMount: function() {
    this.loadData();
  },
  loadData: function() {
    fetch('http://localhost:8000/test')
      .then((response) => {
          if (response.status >= 400) {
              throw new Error("Bad response from server");
          }
          return response.json();
      })
      .then((data) => {
        this.setState({message: data.message});
      });
  },
  render: function() {
      return (
        <div className='message'>
          Message: {this.state.message}
        </div>
      )
  }
});

module.exports = App;
