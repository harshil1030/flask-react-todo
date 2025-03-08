import React, { useState } from "react";
import axios from "axios";

const API_URL = "http://127.0.0.1:5000/todos";

const TodoForm = ({ onTaskAdded }) => {
  const [task, setTask] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post(API_URL, { task }).then(response => {
      onTaskAdded();
      setTask("");
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={task}
        onChange={(e) => setTask(e.target.value)}
        placeholder="New Task"
      />
      <button type="submit">Add Task</button>
    </form>
  );
};

export default TodoForm;
