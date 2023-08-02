import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorText) {
    // логирование
    console.error(error, errorText);
  }

  render() {
    // рендер оповещения об ошибке
    if (this.state.hasError) {
      return (
        <>
          <div>{this.props.text}</div>
          <button onClick={() => {
            window.location.reload()
          }}>Перезагрузить</button>
        </>
      );
    }

    // иначе рендер дочерних компонентов
    return this.props.children;
  }
}

export default ErrorBoundary;
