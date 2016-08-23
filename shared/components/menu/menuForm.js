import React from 'react';
require('es6-promise').polyfill();
require('isomorphic-fetch');

class MenuForm extends React.Component {
  constructor(props) {
      super(props);
      this.handleRadio = this.handleRadio.bind(this);
      this.handleTitle = this.handleTitle.bind(this);
      this.handleSubmit = this.handleSubmit.bind(this);
      this.state = {
        chef: 1,
        title: '',
        delivery: true
    }
  }


  handleTitle(e) {
    this.setState({title: e.target.value})
  }

  handleRadio(e) {
    this.setState({delivery: e.target.value})
  }

  handleSubmit(e) {
    e.preventDefault();
    console.log(this.state);
    fetch('http://localhost:8000/menus/', {
      method: 'POST',
      headers: new Headers({
      'Content-Type': 'application/json',
      Accept: 'application/json',
    }),
      body: JSON.stringify(this.state)
    }).then(function(res) {
        console.log(res);
      }).then(function(json) {
        console.log(json);
    });
  }

  // componentWillMount: function() {

  render() {
      return (
        <div>
        <form onSubmit={this.handleSubmit}>
          <input type="text" onChange={this.handleTitle}  /><br />
          <fieldset>
            <label htmlFor="DeliveryMethod">Pickup</label>
            <input type="radio" name="DeliveryMethod" value="True" onChange={this.handleRadio} /><br />
            <label htmlFor="DeliveryMethod">Delivery</label>
            <input type="radio" name="DeliveryMethod" value="False" onChange={this.handleRadio} />
          </fieldset>
          <input type="submit" value="Submit" />
        </form>
        </div>
      )
  }

}
export default MenuForm;
