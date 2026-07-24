import "./LoadingSpinner.css";

function LoadingSpinner() {
  return (
    <div className="loading-container">
      <div className="spinner"></div>

      <h3>AI is analyzing your code...</h3>

      <div className="loading-steps">
        <p>Checking syntax...</p>
        <p>Detecting bugs...</p>
        <p>Analyzing complexity...</p>
        <p>Generating explanation...</p>
      </div>
    </div>
  );
}

export default LoadingSpinner;