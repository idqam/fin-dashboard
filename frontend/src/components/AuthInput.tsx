import { useState, type FormEvent } from "react";

interface AuthInputProps {
  label?: string;
  endpoint?: string;
}

export default function AuthInput({
  label = "Email",
  endpoint = "http://127.0.0.1:8000/api/auth/signup",
}: AuthInputProps) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [status, setStatus] = useState<
    "idle" | "loading" | "success" | "error"
  >("idle");

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setStatus("loading");

    try {
      const res = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });

      if (!res.ok) throw new Error("Signup failed");
      setStatus("success");
      setEmail("");
      setPassword("");
    } catch (err) {
      console.error(err);
      setStatus("error");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <form
        onSubmit={handleSubmit}
        className="bg-white shadow-md rounded-2xl p-6 w-80 flex flex-col gap-4"
      >
        <h2 className="text-xl font-semibold text-center">Sign Up</h2>

        <label className="flex flex-col text-sm text-gray-600">
          {label}
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="border p-2 rounded-lg mt-1"
            required
          />
        </label>

        <label className="flex flex-col text-sm text-gray-600">
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="border p-2 rounded-lg mt-1"
            required
          />
        </label>

        <button
          type="submit"
          disabled={status === "loading"}
          className="bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50"
        >
          {status === "loading" ? "Creating..." : "Create Account"}
        </button>

        {status === "success" && (
          <p className="text-green-600 text-sm text-center">Success ✅</p>
        )}
        {status === "error" && (
          <p className="text-red-600 text-sm text-center">
            Something went wrong ❌
          </p>
        )}
      </form>
    </div>
  );
}
