import Navbar from "@/components/navbar"
import Guidebook from "@/components/guidebook"

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
          Make sure that your image looks like the following to correctly write your code!
        </p>
      </div>
      <Guidebook />
    </main>
  )
}
