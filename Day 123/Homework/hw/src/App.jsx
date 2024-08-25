import Api from "./Components/Api";
import AutoCounter from "./Components/AutoCounter";
import ClickAlert from "./Components/ClickAlert";
import Counter from "./Components/Counter";
import DataFetch from "./Components/DataFetch";
import Timer from "./Components/Timer";
import Title from "./Components/Title";
import Tracker from "./Components/Tracker";
import Visibility from "./Components/Visibility";
import WindowResize from "./Components/WindowResize";

export default function App(){
  return (
    <main>
      <Counter />
      <Title />
      <Visibility />
      <Api />
      <AutoCounter />
      <Tracker />
      <WindowResize />
      <ClickAlert />
      <DataFetch />
      <Timer />
    </main>
  )
}