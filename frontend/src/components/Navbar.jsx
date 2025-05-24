import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="bg-gray-800 text-white px-4 py-2 flex gap-4">
      <Link to="/" className="hover:text-green-400">Home</Link>
      <Link to="/about" className="hover:text-green-400">About</Link>
    </nav>
  )
}
