import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");

  const handleShorten = async () => {

    const response = await fetch("http://localhost:8000/api/v1/shorten", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        long_url: url
      })
    });
    const data = await response.json();
    setShortUrl(data.short_url);
  };

  return (
    <div>
      <h1>URL Shortener</h1>

      <input
        type="text"
        placeholder="Enter URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />
      <button onClick={handleShorten}>Shorten URL</button>

      {shortUrl && (
        <div>
          <p>Short URL:</p>
          <a href={shortUrl}>{shortUrl}</a>
        </div>
      )}
    </div>
  );
}

export default App;