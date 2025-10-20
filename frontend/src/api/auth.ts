/* eslint-disable @typescript-eslint/no-explicit-any */
export async function signUp(email: any, password: any) {
  const res = await fetch("/api/auth/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });

  if (!res.ok) throw new Error("Signup failed");
  return await res.json();
}
