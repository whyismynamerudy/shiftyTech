import Navbar from "@/components/navbar"

export default function Install() {
  return (
    <main>
      <Navbar />
      <div className="flex flex-col m-3 p-9 text-center">
        <h1 className="pl-9 font-han text-7xl">
          INTERPRETIVE DANCE <br /> OR PYTHON INTERPRETER?
        </h1>
        <h2 className="pl-9 font-han text-5xl">
          YOU CHOOSE!
        </h2>
        <p className="pt-5 pl-9 font-lato text-xl">
            To demo our project, go to our git repository (upper right corner), clone the project and run main.py in the root folder. Use the guide tab to see what you will be able to write with Shifty Tech. You will need to have your own Mylvis and serverless ini to run this as well.
        </p>
        <div className="flex text-center justify-center align-items-center pt-5">
        <iframe className="rounded-lg shadow-xl" width="900" height="510" src="https://www.youtube.com/embed/30Apn-MZtR8?si=UveCVWuR1P88zJkP" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
        </div>
      </div>
    </main>
  )
}
