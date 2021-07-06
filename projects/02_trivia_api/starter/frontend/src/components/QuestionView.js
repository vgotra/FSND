import React, { Component } from 'react';

import '../stylesheets/App.css';
import Question from './Question';
import Search from './Search';

class QuestionView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      questions: [],
      page: 1,
      totalQuestions: 0,
      categories: [],
      currentCategory: null,
    }
  }

  componentDidMount() {
    this.getQuestions();
  }

  getQuestions = () => {
    fetch(`/api/questions/${this.state.page}`, {
      method: 'GET'
    })
      .then(response => response.json())
      .then(result => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          categories: result.categories,
          currentCategory: result.current_category
        });
      })
      .catch(error => {
        console.error(error);
        alert('Unable to load questions. Please try your request again')
      });
  }

  selectPage(num) {
    this.setState({ page: num }, () => this.getQuestions());
  }

  createPagination() {
    let pageNumbers = [];
    let maxPage = Math.ceil(this.state.totalQuestions / 10)
    for (let i = 1; i <= maxPage; i++) {
      pageNumbers.push(
        <span
          key={i}
          className={`page-num ${i === this.state.page ? 'active' : ''}`}
          onClick={() => { this.selectPage(i) }}>{i}
        </span>)
    }
    return pageNumbers;
  }

  getByCategory = (id) => {
    fetch(`/api/categories/${id}/questions`, {
      method: 'GET'
    })
      .then(response => response.json())
      .then(result => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category
        });
      })
      .catch(error => {
        console.error(error);
        alert('Unable to load questions. Please try your request again');
      });
  }

  submitSearch = (searchTerm) => {
    fetch(`/api/questions/search/${encodeURIComponent(searchTerm)}`, {
      method: 'GET'
    })
      .then(response => response.json())
      .then(result => {
        this.setState({
          questions: result.questions,
          totalQuestions: result.total_questions,
          currentCategory: result.current_category
        });
      })
      .catch(error => {
        console.error(error);
        alert('Unable to load questions. Please try your request again');
      });
  }

  questionAction = (id) => (action) => {
    if (action === 'DELETE') {
      if (window.confirm('are you sure you want to delete the question?')) {
        fetch(`/api/questions/${id}`, {
          method: 'DELETE'
        })
          .then(response => response.json())
          .then(result => {
            this.getQuestions();
          })
          .catch(error => {
            console.error(error);
            alert('Unable to load questions. Please try your request again')
          });
      }
    }
  }

  render() {
    return (
      <div className="question-view">
        <div className="categories-list">
          <h2 onClick={() => { this.getQuestions() }}>Categories</h2>
          <ul>
            {this.state.categories.map(category => (
              <li key={category.id} onClick={() => { this.getByCategory(category.id) }}>
                {category.type}
                <img className="category" alt="Category" src={`${category.type.toLowerCase()}.svg`} />
              </li>
            ))}
          </ul>
          <Search submitSearch={this.submitSearch} />
        </div>
        <div className="questions-list">
          <h2>Questions</h2>
          {this.state.questions.map(question => (
            <Question
              key={question.id}
              question={question.question}
              answer={question.answer}
              category={this.state.categories.find(x => x.id === question.category)}
              difficulty={question.difficulty}
              questionAction={this.questionAction(question.id)}
            />
          ))}
          <div className="pagination-menu">
            {this.createPagination()}
          </div>
        </div>

      </div>
    );
  }
}

export default QuestionView;
