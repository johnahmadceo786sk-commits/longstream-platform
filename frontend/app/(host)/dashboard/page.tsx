"use client"

import UploadForm from "../../components/UploadForm"

export default function UploadPage() {
  return (
    <div className="p-10 max-w-3xl mx-auto">

      <h1 className="text-3xl font-bold mb-6">
        Upload Video
      </h1>

      <UploadForm />

    </div>
  )
}