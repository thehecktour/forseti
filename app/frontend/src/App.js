import React from "react";
import { useEffect, useState } from "react";
import api from "./Api";

function App() {
  
  useEffect(() => {
    api
      .get("/clickgb/id")
      .then((response) => setUser(response.data))
      .catch((err) => {
        console.error("ops! ocorreu um erro" + err);
      });
  }, []);

  const [user, setUser] = useState();

  return (
    <div className="App">
      <p>Usuário: {user?.name}</p>
    </div>
  );
}

export default App;
