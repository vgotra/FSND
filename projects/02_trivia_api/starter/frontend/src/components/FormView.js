import React, { Component } from 'react';

import '../stylesheets/FormView.css';

class FormView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      question: "",
      answer: "",
      difficulty: 1,
      category: 1,
      categories: []
    }
  }

  componentDidMount() {
    fetch(`/api/categories`, {
      method: 'GET'
    })
      .then(response => response.json())
      .then(result => {
        this.setState({ categories: result.categories });
      })
      .catch(error => {
        console.error(error);
        alert('Unable to load categories. Please try your request again');
      });
  }


  submitQuestion = (event) => {
    event.preventDefault();
    fetch('/api/questions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        question: this.state.question,
        answer: this.state.answer,
        difficulty: this.state.difficulty,
        category: this.state.category
      }),
    })
      .then(response => response.json())
      .then(result => {
        document.getElementById("add-question-form").reset();
      })
      .catch((error) => {
        console.error(error);
        alert('Unable to add question. Please try your request again');
      });
  }

  handleChange = (event) => {
    this.setState({ [event.target.name]: event.target.value })
  }

  render() {
    return (
      <div id="add-form">
        <h2>Add a New Trivia Question</h2>
        <form className="form-view" id="add-question-form" onSubmit={this.submitQuestion}>
          <label>
            Question:
            <input type="text" name="question" onChange={this.handleChange} />
          </label>
          <label>
            Answer:
            <input type="text" name="answer" onChange={this.handleChange} />
          </label>
          <label>
            Difficulty:
            <select name="difficulty" onChange={this.handleChange}>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="4">4</option>
              <option value="5">5</option>
            </select>
          </label>
          <label>
            Category:
            <select name="category" onChange={this.handleChange}>
              {this.state.categories.map(category => {
                return (
                  <option key={category.id} value={category.id}>{category.type}</option>
                )
              })}
            </select>
          </label>
          <input type="submit" className="button" value="Submit" />
        </form>
      </div>
    );
  }
}

export default FormView;
