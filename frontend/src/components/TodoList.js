import React, { useEffect, useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:5000/todos";

const TodoList = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axios.get(API_URL)
      .then(response => setTodos(response.data))
      .catch(error => console.error(error));
  }, []);

  const handleComplete = (id) => {
    axios.put(`${API_URL}/${id}`).then(() => {
      setTodos(todos.map(todo => (todo.id === id ? { ...todo, completed: true } : todo)));
    });
  };

  const handleDelete = (id) => {
    axios.delete(`${API_URL}/${id}`).then(() => {
      setTodos(todos.filter(todo => todo.id !== id));
    });
  };

  return (
    <div>
      <h2>To-Do List</h2>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            {todo.task} {todo.completed ? "✅" : ""}
            <button onClick={() => handleComplete(todo.id)}>Complete</button>
            <button onClick={() => handleDelete(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
