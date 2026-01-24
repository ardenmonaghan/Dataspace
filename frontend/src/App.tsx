
import './styles/App.css'
import Sidebar from './components/Sidebar'

function App() {
  return (
    <div className="app-container">
      <Sidebar />
      <div className="main-content">
        <p>Welcome to Dataspace</p>
      </div>
    </div>
  )
}

export default App
