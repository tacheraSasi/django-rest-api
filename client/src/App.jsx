import React ,{ useState } from 'react'
import './App.css'
import Books from './components/Books'
import BookForm from './components/BookForm'

function App() {

  return (
    <>
      <h1>Books Data from django api</h1>
      <BookForm />
      <Books/>
    </>
  )
}

export default App
