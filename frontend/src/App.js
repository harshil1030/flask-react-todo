import React, { useState } from "react";
import TodoList from "./components/TodoList";
import TodoForm from "./components/TodoForm";

const App = () => {
  const [update, setUpdate] = useState(false);

  return (
    <div>
      <h1>To-Do App</h1>
      <TodoForm onTaskAdded={() => setUpdate(!update)} />
      <TodoList key={update} />
    </div>
  );
};

export default App;
