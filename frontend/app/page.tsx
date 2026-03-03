import Link from "next/link";

export default function Home() {
  return (
    <div style={{ padding: 40 }}>
      <h1>LongStream Platform</h1>
      <p>Professional Long Video Streaming System</p>

      <div style={{ marginTop: 20 }}>
        <Link href="/search">Public Portal</Link>
        <br />
        <Link href="/login">Host Portal</Link>
      </div>
    </div>
  );
}