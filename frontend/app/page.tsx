import Link from "next/link"

export default function HomePage() {
  return (
    <div>
      <h1>LongStream Platform</h1>

      <p>Share and watch long-duration videos without limits.</p>

      <div style={{ marginTop: 20 }}>
        <Link href="/search">Search Videos</Link>
      </div>
    </div>
  )
}