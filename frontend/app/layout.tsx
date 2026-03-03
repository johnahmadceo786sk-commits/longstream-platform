export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body style={{ fontFamily: "sans-serif", background: "#f4f4f4" }}>
        {children}
      </body>
    </html>
  );
}