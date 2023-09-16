import Navbar from "@/components/navbar"

export default function Home() {
  return (
    <main>
      <Navbar />
     <div className="flex flex-row p-9">
      <div className="basis-1/2 m-3">

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
      </div>
     </div>
    </main>
  )
}
