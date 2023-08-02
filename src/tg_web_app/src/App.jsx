import React from "react";
import "./App.css";
import ErrorBoundary from './ErrorBoundary';
import Header from "./components/Header/Header";
import Main from "./pages/Main/Main";

function App() {
  // const [smoothButtonsTransition, _] = React.useState(false);

  return (
    // <WebAppProvider options={{ smoothButtonsTransition }}>
    <div className="container">
      <ErrorBoundary text="Что-то пошло не так...">
        <Header />
        <Main />
      </ErrorBoundary>
    </div>
    // </WebAppProvider>
  );
}

export default App;
