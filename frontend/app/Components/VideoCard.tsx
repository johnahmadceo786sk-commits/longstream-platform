import Link from "next/link"

export default function VideoCard({ video }: any) {
  return (
    <div
      style={{
        border: "1px solid #334155",
        padding: 16,
        marginBottom: 12
      }}
    >
      <h3>{video.title}</h3>

      <Link href={`/watch/${video.id}`}>Watch</Link>
    </div>
  )
}