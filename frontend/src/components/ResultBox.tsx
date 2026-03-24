import { useState } from "react";

export default function ResultBox({ shortUrl }: { shortUrl: string }) {
  const [copied, setCopied] = useState(false);

  const copy = async () => {
    await navigator.clipboard.writeText(shortUrl);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  };

  if (!shortUrl) return null;

  return (
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

        <div className="copy-btn" onClick={copy}>
          {copied ? "✓" : "Copy"}
        </div>
      </div>
    </div>
  );
}