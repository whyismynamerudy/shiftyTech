import Navbar from "@/components/navbar"

export default function Home() {
  return (
    <main>
      <Navbar />
     <div className="flex flex-row p-9">
      <div className="basis-1/2 flex flex-col m-3">
        <iframe className="rounded-lg shadow-xl" width="660" height="370" src="https://www.youtube.com/embed/D0PfzELt5h8?si=eT_FUEePvCMPzZdH" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"></iframe>
        <p className="pt-3 font-lato text-xl">
          Created during Hack the North 2023
        </p>
      </div>
      <div className="basis-1/2 flex flex-col m-3 text-right">
        <h1 className="pl-9 font-han text-7xl">
          DANCE DANCE REVOLUTIONIZE
        </h1>
        <h2 className="pl-9 font-han text-5xl">
          THE WAY YOU CODE
        </h2>
        <p className="pt-5 pl-9 font-lato text-xl">
          Sick of excruciating back pain and the constant grindset? Let yourself have fun and loosen up those muscles by dancing your work away!
        </p>
        <a className="pt-5" href="/demo">
          <button className="text-pink bg-teal hover:bg-teal-hover py-4 px-6 rounded-lg shadow-xl">
            WATCH DEMO
          </button>
        </a>
        <a className="pt-5" href="/guide">
          <button className="text-pink bg-crimson hover:bg-crimson-hover py-2 px-4 rounded-lg shadow-xl">
            GUIDEBOOK
          </button>
        </a>
      </div>
     </div>
    </main>
  )
}
