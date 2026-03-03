"use client";

import { useState } from "react";
import { api } from "@/app/lib/api";

export default function UploadForm() {
  const [title, setTitle] = useState("");
  const [file, setFile] = useState<any>(null);

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("title", title);
    formData.append("file", file);

    const token = localStorage.getItem("token");

    await api.post("/host/upload", formData, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    });

    alert("Upload started");
  };

  return (
    <div>
      <input placeholder="Title" onChange={(e) => setTitle(e.target.value)} />
      <input type="file" onChange={(e) => setFile(e.target.files?.[0])} />
      <button onClick={handleUpload}>Upload</button>
    </div>
  );
}