"use client";

import { useState } from "react";

export default function SearchBar({ onSearch }: any) {
  const [query, setQuery] = useState("");

  return (
    <div>
      <input
        placeholder="Search by title"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={() => onSearch(query)}>Search</button>
    </div>
  );
}