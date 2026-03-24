const BASE_URL = "https://url-shortner-p316.onrender.com";

export const shortenUrl = async (longUrl: string) => {
  const res = await fetch(`${BASE_URL}/api/v1/shorten`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ long_url: longUrl }),
  });

  if (!res.ok) throw new Error("Failed");

  return res.json();
};

export const getUrls = async () => {
  const res = await fetch(`${BASE_URL}/api/v1/urls`);

  if (!res.ok) throw new Error("Failed");

  return res.json();
};