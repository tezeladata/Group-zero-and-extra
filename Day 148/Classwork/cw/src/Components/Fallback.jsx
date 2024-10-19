const Fallback = ({ resetErrorBoundary }) => {
  return (
    <div className="h-screen w-screen flex items-center justify-center">
      <h1>This is fallback component</h1>
      <button onClick={resetErrorBoundary}>Reset</button>
    </div>
  );
};

export default Fallback;