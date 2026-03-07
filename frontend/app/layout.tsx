import React from "react"

export default function RootLayout({
  children
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body
        style={{
          margin: 0,
          fontFamily: "system-ui",
          background: "#0f172a",
          color: "#fff"
        }}
      >
        <header
          style={{
            padding: 20,
            borderBottom: "1px solid #334155",
            display: "flex",
            justifyContent: "space-between"
          }}
        >
          <h2>LongStream</h2>
        </header>

        <main style={{ padding: 24 }}>{children}</main>
      </body>
    </html>
  )
}