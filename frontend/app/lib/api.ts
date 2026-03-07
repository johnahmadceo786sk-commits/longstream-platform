const API = "http://localhost:8000"

export async function searchVideos(query: string) {
  const res = await fetch(`${API}/search?query=${query}`)
  return res.json()
}

export async function uploadVideo(file: File) {
  const form = new FormData()
  form.append("file", file)

  await fetch(`${API}/host/upload`, {
    method: "POST",
    body: form
  })
}