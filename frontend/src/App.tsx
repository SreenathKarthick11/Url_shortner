import { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading,setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleShorten = async () => {

    if(!url) return;
    setLoading(true);
    setError("");

    try {
    const response = await fetch("http://localhost:8000/api/v1/shorten", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        long_url: url
      })
    });

    if (!response.ok) {
      throw new Error("Failed to shorten URL");
    }

    const data = await response.json();
    setShortUrl(data.short_url);

    } catch (err) {
      setError("Something went wrong. Try again.");
      
    } finally {      
      setLoading(false);
    }
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
      <button onClick={handleShorten} disabled={loading}>
        {loading ? "Shortening..." : "Shorten URL"}
        {error && <p style={{color: "red"}}>{error}</p>}
      </button>

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