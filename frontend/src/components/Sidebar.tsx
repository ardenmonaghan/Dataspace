import { useState } from 'react'
import { FiUpload, FiSettings, FiChevronLeft } from 'react-icons/fi'
import dataspaceImage from '../images/Dataspace.png'
import '../styles/Sidebar.css'

function Sidebar() {
  const [activeMenu, setActiveMenu] = useState<string | null>(null)

  // State for collapsing the sidebar
  const [isCollapsed, setIsCollapsed] = useState(false)

  const handleMenuClick = (menu: string) => {
    setActiveMenu(activeMenu === menu ? null : menu)
  }

  // Function to toggle the sidebar
  const toggleSidebar = () => {
    setIsCollapsed(!isCollapsed)
  }

  return (
    <div className={`sidebar ${isCollapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <img src={dataspaceImage} alt="Dataspace" className="sidebar-logo" />
        <button
          className="collapse-button"
          onClick={toggleSidebar}
          title={isCollapsed ? 'Expand' : 'Collapse'}
        >
          <FiChevronLeft className="collapse-icon" style={{ transform: isCollapsed ? 'rotate(180deg)' : 'rotate(0deg)' }} />
        </button>
      </div>

      <nav className="sidebar-nav">
        {/* Upload Button */}
        <button
          className={`sidebar-button ${activeMenu === 'upload' ? 'active' : ''}`}
          onClick={() => handleMenuClick('upload')}
          title="Upload Files"
        >
          <FiUpload className="sidebar-icon" />
          <span className="sidebar-label">Upload</span>
        </button>

        {/* Settings Button */}
        <button
          className={`sidebar-button ${activeMenu === 'settings' ? 'active' : ''}`}
          onClick={() => handleMenuClick('settings')}
          title="Settings"
        >
          <FiSettings className="sidebar-icon" />
          <span className="sidebar-label">Settings</span>
        </button>
      </nav>
    </div>
  )
}

export default Sidebar
