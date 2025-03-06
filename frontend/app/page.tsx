"use client"; // This makes the component interactive (Client Component)

import { useState } from "react";

export default function Home() {
  const [question, setQuestion] = useState(""); // State for input field
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState("");

  const handleSubmit = async () => {
    if (!question.trim()) {
      setResponse("Please enter a question.");
      return;
    }
    
    setLoading(true);

    try {
      const res = await fetch("/api/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });

      const data = await res.json();
      setResponse(data.message);
    } catch (error) {
      console.error("Error:", error);
      setResponse("Request failed.");
    }

    setLoading(false);
  };

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Ask a Question</h1>

      <input
        type="text"
        placeholder="Enter your question"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        className="mt-4 p-2 border rounded w-full"
      />

      <button
        onClick={handleSubmit}
        className="mt-4 px-4 py-2 bg-blue-500 text-white rounded"
        disabled={loading}
      >
        {loading ? "Submitting..." : "Submit"}
      </button>
      {response && <p className="mt-2">Response: {response}</p>}
    </div>
  );
}
