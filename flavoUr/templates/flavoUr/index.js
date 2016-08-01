var React = require('react')
var ReactDOM = require('react-dom')
require("../../static/css/style.css");
var Hello = React.createClass ({
    render: function() {
        return (
            <h1>
            SUP, React!
            </h1>
        )
    }
})

ReactDOM.render(<Hello />, document.getElementById('container'))
