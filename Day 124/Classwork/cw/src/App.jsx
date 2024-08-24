import { useEffect, useState } from "react"
import "./App.css"

const apiUrl = 'https://api.thenewsapi.com/v1/news/top?api_token=DL7KKpOInhKaXll5zNjCw6e3r0MU01YkKqjkYYKw&locale=us&limit=3';

export default function App() {
  const [newsData, setNewsData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(apiUrl);
      const data = await response.json();
      
      setNewsData(data.data);
    }

    fetchData()
  }, []);

  return (
    <main>
      <h1>news</h1>
      <hr />


      <section id="main-section">
        {
          newsData?.map((item, index) => {
            return (
              <article key={index}>
                <hr />

                <h2>{item.title}</h2>

                <div id="article-cont">
                  <div id="part1">
                    <img src={item.image_url} />
                  </div>
                  <div id="part2">
                    <p>{item.description}</p>
                    <p>{item.snippet}</p>
                    
                    <a href={item.url} target="_blank">See more</a>
                  </div>
                </div>

                <hr />
              </article>
            )
          })
        }
      </section>
    </main>
  )
}