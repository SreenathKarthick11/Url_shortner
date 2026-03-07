import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");

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
    console.log(data);
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
    </div>
  );
}

export default App;