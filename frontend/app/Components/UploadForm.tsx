"use client"

import { useState } from "react"
import { uploadVideo } from "@/lib/api"

export default function UploadForm() {
  const [file, setFile] = useState<File | null>(null)

  async function handleUpload() {
    if (!file) return

    await uploadVideo(file)

    alert("Upload complete")
  }

  return (
    <div>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files?.[0] || null)}
      />

      <button onClick={handleUpload}>Upload</button>
    </div>
  )
}