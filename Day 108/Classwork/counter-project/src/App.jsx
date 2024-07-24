import Counter from "./components/Counter.jsx"

// This is component, so it starts with capital letter
// Component should only return one jsx, for example div
const App = () => {
  return (
    <div>
      <Counter />
      <Counter />
      <Counter />
    </div>
  )
}

export default App