type Props = {
  url: string;
  setUrl: (v: string) => void;
  onSubmit: () => void;
  loading: boolean;
};

export default function UrlInput({ url, setUrl, onSubmit, loading }: Props) {
  return (
    <>
      <input
        className="url-input"
        type="text"
        placeholder="Enter URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && onSubmit()}
      />

      <button
        className="shorten-btn"
        onClick={onSubmit}
        disabled={loading}
      >
        {loading ? "Shortening..." : "Shorten URL"}
      </button>
    </>
  );
}