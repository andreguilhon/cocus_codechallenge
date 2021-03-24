import React, { Component } from "react";
import { render } from "react-dom";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      quotes: [],
      loaded: false,
      placeholder: "Loading",
      most_common_character: {}
    };
    this.handleClick = this.handleClick.bind(this);
  }

  componentDidMount() {
    this.fetchInitialQuotes()
    this.fetchMostCommonCharacter()
  }
  fetchMostCommonCharacter() {
    fetch("quotes/most_common_character/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            most_common_character: data,
            loaded: true,
          };
        });
      });
  }

  handleClick(e) {
    this.fetchData();
  }

  fetchData() {
    fetch("quotes/get_many/1/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(quote => {
        this.setState(() => {
          return {
            quotes: this.state.quotes.concat(quote),
            loaded: true,
          };
        });
      });
  }

  fetchInitialQuotes() {
    fetch("quotes/get_many/5/")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(quotes => {
        this.setState(() => {
          return {
            quotes,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <div>
        <div>
          <div className="row" style={{ margin: "20px" }}>
            <div className="column main" >
              <h2>The most common character in the database is <b>{this.state.most_common_character.most_common_character}</b></h2>
              <p>It is the most frequent character in {this.state.most_common_character.count} quotes.</p>
            </div>
          </div>
          {this.state.quotes.map(quote => {
            return (
              <div className="row" style={{ margin: "20px" }} key={quote.line_number}>
                <div className="column quote" >
                  <h2>{quote.line_content}</h2>
                  <p>The most frequent character in this quote is {quote.most_common_character}</p>
                </div>
              </div>
            );
          })}
          <div className="row">
            <div className="column" style={{ textAlign: "center" }}>
              <button onClick={this.handleClick} className="button">Hit me another one!</button>
            </div>
          </div>
        </div>

      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);