import { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [copied, setCopied] = useState(false);

  const isValidUrl = (url: string) => {
    try {
      new URL(url.startsWith("http") ? url : `https://${url}`);
      return true;
    } catch {
      return false;
    }
  };

  const handleShorten = async () => {
    if (!url) {
      setError("Enter a URL");
      return;
    }

    if (!isValidUrl(url)) {
      setError("Invalid URL");
      return;
    }

    setLoading(true);
    setError("");
    setShortUrl("");

    try {
      const response = await fetch(
        "https://url-shortner-p316.onrender.com/api/v1/shorten",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            long_url: url,
          }),
        }
      );

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

  const copyToClipboard = async () => {
    await navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  return (
    <div className="container">
      <h1 className="title">URL Shortener</h1>

      <input
        className="url-input"
        type="text"
        placeholder="Enter URL"
        value={url}
        onChange={(e) => {
          setUrl(e.target.value);
          setShortUrl("");
          setError("");
        }}
        onKeyDown={(e) => {
          if (e.key === "Enter") handleShorten();
        }}
      />

      <button
        className="shorten-btn"
        onClick={handleShorten}
        disabled={loading}
      >
        {loading ? "Shortening..." : "Shorten URL"}
      </button>

      {error && <p className="error">{error}</p>}

      {shortUrl && (
        <div className="result">
          <div className="result-row">
            <a
              href={shortUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="short-link"
            >
              {shortUrl}
            </a>

            <div className="copy-btn" onClick={copyToClipboard}>
              {copied ? "✓" : "Copy"}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;