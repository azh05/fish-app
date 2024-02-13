//
//  ContentView.swift
//  videodemo
//
//  Created by Anthony Zhao on 2/11/24.
//

enum Emoji: String, CaseIterable {
    case 😭, 🫃, 🇮🇳
}

import SwiftUI

struct ContentView: View {
    @State var selection: Emoji = .🇮🇳
    var body: some View {
        
        NavigationView {
            ZStack {
                Image("portrait").resizable().cornerRadius(/*@START_MENU_TOKEN@*/10.0/*@END_MENU_TOKEN@*/)
                    .aspectRatio(contentMode: .fit)
                    .padding()
                
                VStack{
                    Text(selection.rawValue)
                        .font(.system(size: 100))
                    Picker("Select Emoji", selection: $selection) {
                        ForEach(Emoji.allCases, id: \.self) { emoji in
                            Text(emoji.rawValue)
                        }
                    }
                    .pickerStyle(.segmented).padding()

                    
                        .navigationTitle("Men!")
                }
                .padding()
            }
        }
    }
}

#Preview {
    ContentView()
}
