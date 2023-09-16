import Navbar from "@/components/navbar"

export default function Guide() {
  return (
    <main>
      <Navbar />
      <div className="flex flex-col m-3 p-9">
        <h1 className="pl-9 font-han text-7xl text-center">
          YOUR GO-TO GUIDE FOR
        </h1>
        <h2 className="pl-9 font-han text-5xl text-center">
          SHIFTY TECH
        </h2>
        <p className="pt-5 pl-9 font-lato text-xl text-center">
          Sick of excruciating back pain and the constant grindset? Let yourself have fun and loosen up those muscles by dancing your work away!
        </p>
      </div>
    </main>
  )
}
